import logging
import os

class Hedge:
    def __init__(self, repoRootPath):
        self.repoRootPath = repoRootPath

    def preflight(self, agent, params):
        agent.runCommand('add-apt-repository -y ppa:neovim-ppa/stable')
        agent.runCommand('apt-get update')

    def vim(self, agent, params):

        #NOTE: This method has limitations, for example it will
        #      only update to certain version preventing lazyvim from working
        #      use target neovim to get neovim installed manually to higher version

        if not os.environ['HOME']:
            logging.error('HOME environment variable is not define, cannot continue')
            return
        home = os.environ['HOME']
        agent.ensurePackages(['neovim'])
        
        agent.ensureFile('/vim/.vimrc', f"{home}/.vimrc")

    def nvim(self, agent, params):
        tmp = agent.getTempPath()
        agent.runCommand(f"wget https://github.com/neovim/neovim/releases/download/v0.11.4/nvim-linux-x86_64.tar.gz -o {tmp}/nvim-linux-x86_64.tar.gz")
        logging.info(f"Extracted to {tmp}/nvim-linux-x86_64.tar.gz")


    def lazyvim(self, agent, params):
        pass        

    def k8s_helper(self, agent, params):
        if not os.environ['HOME']:
            logging.error('HOME environment variable is not define, cannot continue')
            return
        home = os.environ['HOME']    
        agent.ensureFile('/k8s/fwk8s.py', f"{home}/scripts/fwk8s.py")
        
