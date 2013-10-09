import Image
import imagehash
import subprocess

hash1 = imagehash.phash(Image.open( '1.png') )
hash2 = imagehash.phash(Image.open( '2.png') )
hash3 = imagehash.phash(Image.open( '3.png') )
hash4 = imagehash.phash(Image.open( '4.png') )

print hash1 - hash2
print hash2 - hash3
print hash3 - hash4

alist = ['1.png', '2.png', '3.png', '4.png', '5.png']
alist.insert(0,'convert')
alist.append('-delay')
alist.append('200')
alist.append('image-animated.gif')
subprocess.call(alist)
