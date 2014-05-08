import json
import human_curl as requests
artistNames = ['Methuselah', 'FAUX/BLU', 'T!BE', 'b00n', 'nocon', 'AndMyLoafers', 'EdEthics', 'delusion.', 'magoni', 'Naota', 'Eelahno', 'Manitee', 'fsn', 'GLiPH', 'Feels', 'fleece', 'terminoir', 'jPolo', 'Renja', 'Kez the Dude']
artistSites = ['https://soundcloud.com/meth420', 'https://soundcloud.com/fauxblu', 'https://soundcloud.com/ethan-barer', 'https://soundcloud.com/z05', 'https://soundcloud.com/nocondj', 'https://soundcloud.com/anddrew-eddward', 'https://soundcloud.com/edethics', 'https://soundcloud.com/itsdelusion', 'https://soundcloud.com/magoni', 'https://soundcloud.com/elm6', 'https://soundcloud.com/eelahno', 'https://soundcloud.com/robert-dingus', 'https://soundcloud.com/579', 'https://soundcloud.com/gliph', 'https://soundcloud.com/feels', 'https://soundcloud.com/fleece', 'https://soundcloud.com/terminoir', 'https://soundcloud.com/jpolobeats', 'https://soundcloud.com/amant9000', 'https://soundcloud.com/kez-the-dude-charles']
artistPics = ['meth.jpg', 'fauxblu.jpg', 'tibe.jpg', 'b00n.jpg', 'nocon.jpg', 'andmyloafers.jpg', 'ed.jpg', 'delusion.jpg', 'magoni.jpg', 'naota.jpg', 'eelahno.jpg', 'dingus.jpg', 'fsn.jpg', 'gliph.jpg', 'feels.jpg', 'fleece.jpg', 'terminoir.jpg', 'jpolo.jpg', 'renja.jpg', 'Kez.jpg']

for x in range(0,len(artistNames)):
  f = open ('2014-05-08-' + str(artistPics[x])[:-4].lower() + '.md', 'w')
  f.write('---\n')
  f.write('layout: artist\n')
  f.write('title: ' + artistNames[x] + '\n')
  f.write('category: artists' + '\n')
  f.write('image: ' + artistPics[x] + '\n')
  f.write('---\n')
  f.write('<p>artist description here</p>\n')
  r = requests.get('http://api.soundcloud.com/resolve.json?url=' + artistSites[x] + '&client_id=5baf9e59272a30dcdaa6683e69cd3e8a', allow_redirects=True)
  data = json.loads(r.content)
  f.write('<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/users/' + str(data['id']) + '&amp;color=999999&amp;auto_play=false&amp;hide_related=true&amp;show_artwork=false"></iframe>\n')
  f.close()
  print x + '/' + str(len(artistNames))
