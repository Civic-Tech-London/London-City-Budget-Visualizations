# London-City-Budget-Visualizations
https://drive.google.com/file/d/11mwgkpFSpDYLpQK8p0Oj-qspqgtDOBHc/preview

## Required Libraries
### Python
* pdfplumber - `pip install pdfplumber`
* pandas - `pip install pandas`

## Required packages
### NPM
#### Windows (powershell)
~~~
# installs fnm (Fast Node Manager)
winget install Schniz.fnm

# configure fnm environment
fnm env --use-on-cd | Out-String | Invoke-Expression

# download and install Node.js
fnm use --install-if-missing 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.17.0`

# verifies the right npm version is in the environment
npm -v # should print `10.8.2`
~~~
#### Mac/Linux (bash)
~~~
# installs fnm (Fast Node Manager)
curl -fsSL https://fnm.vercel.app/install | bash

# activate fnm
source ~/.bashrc

# download and install Node.js
fnm use --install-if-missing 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.17.0`

# verifies the right npm version is in the environment
npm -v # should print `10.8.2`
~~~