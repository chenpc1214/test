travel = {'張家界':{'state':'湖南省',
                    'attraction':'天門山, 大峽谷'},
          '九寨溝':{'state':'四川省',
                    'attraction':'熊貓海, 箭竹海'},
          '黃山':{'state':'安徽省',
                  'attraction':'天都峰, 蓬萊三島'},
          '武夷山':{'state':'福建省',
                    'attraction':'天遊峰, 桃源洞'},
          '敦煌':{'state':'甘肅省',
                  'attraction':'石窟, 月牙泉'}}

for loc, info in travel.items( ):
    
    print("旅遊地點 = ", loc)
    print("省份     = ", info['state'])          
    print("景點     = ", info['attraction'])     

