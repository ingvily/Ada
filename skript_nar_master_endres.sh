# Litt tungvint, med må nesten bare sørge for å isolere commits 
# og cherrypicke den man vil

# git checkout Idunn
# git cherry-pick (commit 55b9bbe5da59b84d)
# git push
# git checkout Odin
# git cherry-pick (commit 55b9bbe5da59b84d)
# git push
# git checkout Tor
# git cherry-pick (commit 55b9bbe5da59b84d)
# git push
# git checkout Frøya
# git cherry-pick (commit 55b9bbe5da59b84d)
# git push
# git checkout Loke
# git cherry-pick (commit 55b9bbe5da59b84d)
# git push


# eller: det er bare shell-skritpene og robotene som blir endret på
# kopiere over de når det skjer noe, kanskje? 


# Oppdaterer branchen idunn: 
git checkout Idunn 

git checkout master Robots/easy.py
git checkout master Robots/medium.py
git checkout master Robots/hard.py

git checkout master main.sh
git checkout Spill_Lett.sh
git checkout Spill_Middels.sh
git checkout Spill_Vanskelig.sh

git push 


# Oppdaterer branchen Odin: 
git checkout Odin 

git checkout master Robots/easy.py
git checkout master Robots/medium.py
git checkout master Robots/hard.py

git checkout master main.sh
git checkout Spill_Lett.sh
git checkout Spill_Middels.sh
git checkout Spill_Vanskelig.sh

git push 


# Oppdaterer branchen Frøya: 
git checkout Frøya 

git checkout master Robots/easy.py
git checkout master Robots/medium.py
git checkout master Robots/hard.py

git checkout master main.sh
git checkout Spill_Lett.sh
git checkout Spill_Middels.sh
git checkout Spill_Vanskelig.sh

git push 


# Oppdaterer branchen Tor: 
git checkout Tor 

git checkout master Robots/easy.py
git checkout master Robots/medium.py
git checkout master Robots/hard.py

git checkout master main.sh
git checkout Spill_Lett.sh
git checkout Spill_Middels.sh
git checkout Spill_Vanskelig.sh

git push 


# Oppdaterer branchen Loke: 
git checkout Loke 

git checkout master Robots/easy.py
git checkout master Robots/medium.py
git checkout master Robots/hard.py

git checkout master main.sh
git checkout Spill_Lett.sh
git checkout Spill_Middels.sh
git checkout Spill_Vanskelig.sh

git push 
