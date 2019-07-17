from pathlib import Path
SYSTEMD_SERVICE = """\
[Service]
Type=forking
PIDFile=%h/.devpi/server/.xproc/devpi-server/xprocess.PID
Restart=always
ExecStart=%h/.local/venvs/devpi/bin/devpi-server  --start
ExecStop=%h/.local/venvs/devpi/bin/devpi-server  --stop
SuccessExitStatus=SIGKILL

[Install]
WantedBy=default.target
"""

STATE_FILE = Path("~/.devpi/server/.serverversion")


def ensure(env):
    venv = env.ensure_venv("devpi")
    venv.ensure_packages(["devpi-server", "devpi-web", "devpi-client"])
    env.ensure_linked_binary_from(venv, "bin/devpi")
    if not env.has_file(STATE_FILE):
        env.run_command("devpi-server", "--init")
        assert STATE_FILE.exists()
    env.systemd_service(
        name="devpi.service",
        scope=SystemdScope.USER,
        start=True,
        enable=True,
        service_file_content=SYSTEMD_SERVICE,
    )
