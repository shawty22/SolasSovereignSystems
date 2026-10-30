from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).parent
out=Path('/Users/dooj/Documents/Codex/2026-10-29/sites-plugin-sites-openai-curated-remote/outputs')
assets=root/'assets'
mint='#80dfbd';bg='#101413';white='#f0f2ef'
paths=['M110 110H382V220H220V580H330V690H110Z','M418 110H690V690H470V580H580V220H418Z','M392 220H408L436 690H364Z']
mark=''.join('<path d="'+p+'"/>' for p in paths)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="110 110 580 580"><g fill="{mint}">{mark}</g></svg>'
(assets/'solas-symbol.svg').write_text(svg)
favicon=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800"><rect width="800" height="800" rx="120" fill="{bg}"/><g fill="{mint}">{mark}</g></svg>'
(assets/'solas-favicon.svg').write_text(favicon)
(out/'solas-logo-coordinated.svg').write_text(favicon)
logo=Image.new('RGB',(800,800),bg);d=ImageDraw.Draw(logo)
for poly in [[(110,110),(382,110),(382,220),(220,220),(220,580),(330,580),(330,690),(110,690)],[(418,110),(690,110),(690,690),(470,690),(470,580),(580,580),(580,220),(418,220)],[(392,220),(408,220),(436,690),(364,690)]]:d.polygon(poly,fill=mint)
logo.save(out/'solas-linkedin-symbol-v3.png')
logo.resize((180,180),Image.Resampling.LANCZOS).save(assets/'solas-touch-icon.png')
fontpath='/System/Library/Fonts/Supplemental/Arial.ttf'
banner=Image.new('RGB',(2256,382),bg);d=ImageDraw.Draw(banner)
font=ImageFont.truetype(fontpath,139)
d.text((650,23),'AI infrastructure.',font=font,fill=white)
d.text((650,181),'Under your control.',font=font,fill=white)
d.rectangle((570,70,576,310),fill=mint)
banner.save(out/'solas-linkedin-banner-readable-v3.png')
card=Image.new('RGB',(1200,630),bg);card.paste(logo.resize((100,100),Image.Resampling.LANCZOS),(50,45));d=ImageDraw.Draw(card)
def txt(x,y,s,size,c=white):d.text((x,y),s,font=ImageFont.truetype(fontpath,size),fill=c)
txt(170,60,'Solas',48);txt(173,116,'S O V E R E I G N  S Y S T E M S',11)
d.line((70,180,1130,180),fill='#303b36')
txt(70,235,'AI infrastructure.',67);txt(70,315,'Under your control.',67)
txt(73,435,'Private & hybrid AI. Advisory through implementation.',22,'#a9b3ae');txt(73,559,'solassovereignsystems.ai',18,mint)
card.save(assets/'social-card-v3.png')
