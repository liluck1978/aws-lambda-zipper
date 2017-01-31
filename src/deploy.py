import os
from src import logger
from subprocess import Popen, PIPE


class Deploy:

    def __init__(self, requirements):
        self._requirements_file = requirements

    def install_requirements(self):

        cmd = None

        # if self._requirements:
        #     logger.debug("Installing requirements found %s in config"
        #               % self._requirements)
        #     cmd = [os.path.join(self._pkg_venv, self._venv_pip),
        #            'install'] + self._requirements

        if os.path.isfile(self._requirements_file):
            # Pip install
            logger.debug("Installing requirements from requirements.txt file")
            cmd = [os.path.join("pip"),
                   "install", "-r", self._requirements_file, "-t", "./"]

        if cmd is not None:
            prc = Popen(cmd, stdout=PIPE, stderr=PIPE)
            stdout, stderr = prc.communicate()
            logger.debug("Pip stdout: %s" % stdout)
            logger.debug("Pip stderr: %s" % stderr)

            if prc.returncode is not 0:
                raise Exception('pip returned unsuccessfully')


if __name__ == '__main__':
    deploy = Deploy('resources/requirements.txt')
    deploy.install_requirements()
