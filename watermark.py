import Image,ImageEnhance
def reduce_opacity(im,opacity):
	assert opacity>=0 and opacity <=1
	if im.mode != 'RGBA':
		im=im.convert('RGBA')
	else:
		im=im.copy()
	alpha=im.split()[3]
	alpha=ImageEnhance.Brightness(alpha).enhance(opacity)
	im.putalpha(alpha)

	return im

def watermark(im,mark,position,opacity=1):
	if opacity<1:
		mark=reduce_opacity(mark,opacity)
	if im.mode !='RGBA':
		im=im.convert('RGBA')
	layer=Image.new('RGBA',im.size,(0,0,0,0))
	if position == 'tile':
		for y in range(0,im.size[0],mark.size[0]):
			for x in range(0,im.size[0],mark.size[0]):
				layer.paste(mark,(x,y))
	elif position=='scale':
		ratio=min(float(im.size[0])/mark.size[0],float(im.size[1])/mark.size[1])
		w=int(mark.size[0] * ratio)
		h=int(mark.size[1] * ratio)
		mark=mark.resize((w,h))
		layer.paste(mark,((im.size[0] - w) /2, (im.size[1] -h )/2))
	else:
		layer.paste(mark,position)

	return Image.composite(layer,im,layer)

def test():
	im=Image.open('d:/tmp/pytest/test.png')
	mark=Image.open('d:/tmp/pytest/overlay.png')
	watermark(im,mark,'tile',0.5).show()
	watermark(im,mark,'scale',0.2).show()
	watermark(im,mark,(100,100),0.5).show()

if __name__=='__main__':
	test()

