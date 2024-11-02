import speedtest

def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()  
    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000  
    ping = st.results.ping  

    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

speed_test()
