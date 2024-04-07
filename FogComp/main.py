import socket
import findNode
import nodeRegist



def main():
    
    
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("172.20.94.189", 8081))

    tcp_server_socket.listen(1)

    while True:
        print("等待一个新的客户端的到来...")
    
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来%s" % str(client_addr))
        
        while True:
            
        
            recv_data = new_client_socket.recv(1024)

            if recv_data:
                rec = recv_data.decode("utf-8","ignore")
                print("请求是:%s" % rec)
                if rec:
                    if rec[:3]=='TSK':
                        findNode.findNode1("task1",1,9,rec)
                        s='TSKt'+findNode.targetCode
                        new_client_socket.send(s.encode('utf-8'))
                    
                    elif rec[:3]=='REG':
                        nodeRegist.nodeRegist1(rec)

                    else :
                        print('Unrecognized')
                
                else:
                    continue


                # 如果recv解堵塞，那么有2种方式：
                # 1. 客户端发送过来数据
                # 2. 客户端调用close导致recv解堵塞
                
            else :
                break

        # 关闭套接字
        # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
        new_client_socket.close()
        print("已经为这个客户端服务完毕。。。。")

    # 如果将监听套接字 关闭了，那么会导致 不能再次等待新客户端的到来，即xxxx.accept就会失败
    tcp_server_socket.close()

if __name__ == "__main__":
    main()



