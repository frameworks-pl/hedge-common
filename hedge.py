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
        agent.runCommand(f"wget https://github.com/neovim/neovim/releases/download/v0.11.4/nvim-linux-x86_64.tar.gz -O {tmp}/nvim-linux-x86_64.tar.gz")
        agent.runCommand(f"tar xzvf {tmp}/nvim-linux-x86_64.tar.gz -C {tmp}")
        agent.runCommand(f"mv {tmp}/nvim-linux-x86_64 /opt/nvim")
        agent.ensureDir("/opt/nvim")

        #backup existing nvim, if there is one
        agent.runCommand("[ ! -e /usr/bin/nvim.old ] && sudo mv /usr/bin/nvim /usr/bin/nvim.old || :")
        agent.runCommand("rm -rf /usr/bin/nvim")

        #link nvim downloaded ot /usr/bin/vim
        agent.runCommand('ln -s /opt/nvim/bin/nvim /usr/bin/nvim')


    def lazyvim(self, agent, params):
        home = os.environ['HOME']

        #just to make a backup
        agent.ensureDir(f"{home}/.config/nvim") 

        #remove dir, as git expect it to not be there
        agent.runCommand(f"rm -rf {home}/.config/nvim")

        agent.runCommand(f"git clone https://github.com/LazyVim/starter {home}/.config/nvim")
        agent.runCommand(f"rm -rf {home}/.config/nvim/.git")

    def k8s_helper(self, agent, params):
        if not os.environ['HOME']:
            logging.error('HOME environment variable is not define, cannot continue')
            return
        home = os.environ['HOME']    
        agent.ensureFile('/k8s/fwk8s.py', f"{home}/scripts/fwk8s.py")
        
