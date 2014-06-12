import json
import human_curl as requests
from os import system
artistNames = ['Methuselah', 'FAUX/BLU', 'T!BE', 'b00n', 'nocon', 'AndMyLoafers', 'EdEthics', 'delusion.', 'magoni', 'Naota', 'Eelahno', 'Manitee', 'fsn', 'GLiPH', 'Feels', 'fleece', 'terminoir', 'jPolo', 'Renja', 'Kez the Dude']
artistSites = ['https://soundcloud.com/meth420', 'https://soundcloud.com/fauxblu', 'https://soundcloud.com/ethan-barer', 'https://soundcloud.com/z05', 'https://soundcloud.com/nocondj', 'https://soundcloud.com/anddrew-eddward', 'https://soundcloud.com/edethics', 'https://soundcloud.com/itsdelusion', 'https://soundcloud.com/magoni', 'https://soundcloud.com/osnaota', 'https://soundcloud.com/eelahno', 'https://soundcloud.com/robert-dingus', 'https://soundcloud.com/579', 'https://soundcloud.com/gliph', 'https://soundcloud.com/feels', 'https://soundcloud.com/fleece', 'https://soundcloud.com/terminoir', 'https://soundcloud.com/jpolobeats', 'https://soundcloud.com/amant9000', 'https://soundcloud.com/kez-the-dude-charles']
artistPics = ['meth.jpg', 'fauxblu.jpg', 'tibe.jpg', 'b00n.jpg', 'nocon.jpg',
              'andmyloafers.jpg', 'ed.jpg', 'delusion.jpg', 'magoni.jpg',
              'naota.jpg', 'eelahno.jpg', 'dingus.jpg', 'fsn.jpg', 'gliph.jpg',
              'feels.jpg', 'fleece.jpg', 'terminoir.jpg', 'jpolo.jpg',
              'renja.jpg', 'Kez.jpg']

for x in range(0, len(artistNames)):
    r = requests.get('http://api.soundcloud.com/resolve.json?url=' +
                     artistSites[x] +
                     '&client_id=5baf9e59272a30dcdaa6683e69cd3e8a', allow_redirects=True)
    data = json.loads(r.content)
    avatar = data['avatar_url']
    avatar = avatar.replace('large', 't500x500')
    args = '-O ' + artistPics[x] + ' ' + avatar
    system("wget " + args)
    print 'wget ' + args
