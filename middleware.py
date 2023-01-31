# oturum sinyalini aldık
def session_check_middleware(get_response):

    def middleware(request):
        if not request.session.session_key: #siteye giren kişinin session key yoksa buna bi session key ver 
            request.session.save()
 # bu sistemin hepsini kopyaladık sadedce üstteki sorguyu yazdık şimdi bunu settings de kaydetmemiz lazım
        
        print(f"SESSİON_KEY:{request.session.session_key}")  
        response = get_response(request)
        


        return response

    return middleware

# not: middleware yapmamızın amacı kullanıcı sadece anasayfadan alışveriş yapmıyabilir iletişim sayfasının kenarında ürün olabilir mesela view yazdıgımız session sadece view etkiliyo ama burdaki middleware yazdıgımız kod bütün projenin içeriklerini kaplıyor  
# not2: context processor benziyor ama middleware den sonra çalışıyor context prossesor context processor daha çok template ile ilgilidir
# middleware ise her şeyi denetliyor
# normal bi kullancı iken siteye girdiysek bi key verilir ama giriş yaptıktan sonra bu key değişiyor    

# bu yüzden eğer login olmuş birinin keyini almak istiyorsak önce login olmamış keyini almamız lazım peki ne için session key değiştiriyor diye sorarsak cart bilgisi için  cart ın altında session_key açıçaz onun altıan atıcaz  