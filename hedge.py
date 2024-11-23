import logging

class Hedge:
    def __init__(self, repoRootPath):
        self.repoRootPath = repoRootPath

    def preflight(self, agent, params):
        agent.runCommand('apt-get update')


    def vim(self, agent, params):
        agent.ensurePackages['neovim']