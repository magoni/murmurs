import json
import human_curl as requests

cypherurls = ['murmurs-weekly-beat-cypher-vol-9', 'murmurs-weekly-beat-cypher-vol-8', 'murmurs-weekly-beat-cypher-vol-7', 'murmurs-cypher-6-mix', 'murmurs-weekly-beat-cypher-vol-5', 'murmurs-weekly-beat-cypher-vol-4', 'murmurs-weekly-beat-cypher-vol-3', 'mm-wbc2', 'mm-wbc1']

for curl in cypherurls:
    r = requests.get('http://api.soundcloud.com/resolve.json?url=' + 'https://soundcloud.com/murmurscollective/' + curl + '/' + '&client_id=5baf9e59272a30dcdaa6683e69cd3e8a', allow_redirects=True)
    data = json.loads(r.content)
    f = open('2014-06-11-' + str(curl).lower() + '.md', 'w')
    f.write('---\n')
    f.write('layout: default\n')
    f.write('title: ' + data['title'] + '\n')
    f.write('category: cyphers ' + '\n')
    f.write('---\n')
    f.write('<iframe width="100%" height="300" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/' + str(data['id']) + '&amp;auto_play=false&amp;hide_related=true&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>\n')
    f.write('<div class="descrip">' + data['description'] + '</div>\n')
    f.close()
    print curl
