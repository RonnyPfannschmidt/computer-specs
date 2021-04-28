

def ensure(env):
    venv = env.ensure_venv("pre-commit")
    venv.ensure_packages(["pre-commit"], update=True)
    env.ensure_linked_binary_from(venv, "bin/pre-commit")
