if [[ ! -e ~/MyConf/fonts/Agave ]]; then
	mkdir ~/MyConf/fonts
	wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/Agave.zip -O ~/Downloads/Agave.zip
	cd ~/Downloads/

	mkdir -p Agave
	unzip Agave.zip -d Agave
	mv Agave ~/MyConf/fonts
fi

if [[ ! -d ~/MyConf/fonts/LXGW ]]; then
	mkdir ~/MyConf/fonts/LXGW
	wget https://github.com/lxgw/LxgwWenKai/releases/download/v1.510/LXGWWenKai-Regular.ttf -O ~/MyConf/fonts/LXGW/LXGWWenKai-Regular.ttf
fi
