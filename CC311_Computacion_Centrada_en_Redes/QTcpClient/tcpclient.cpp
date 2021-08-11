#include "tcpclient.h"
#include "ui_tcpclient.h"

TcpClient::TcpClient(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::TcpClient)
{
    ui->setupUi(this);
    qTcpSocket=new QTcpSocket(this);
    in.setDevice(qTcpSocket);
    //boton salir
    connect(ui->btn_close,&QAbstractButton::clicked,this,&QWidget::close);
    //conect request message
    connect(ui->btn_request,&QAbstractButton::clicked,this,&TcpClient::requestMessage);
    //connect read message
    connect(qTcpSocket,&QIODevice::readyRead,this,&TcpClient::readMessage);
    //connect error
    connect(qTcpSocket,&QAbstractSocket::errorOccurred,this,&TcpClient::showError);


}

TcpClient::~TcpClient()
{
    delete ui;
}

void TcpClient::requestMessage()
{
qInfo()<<"request Message";
QString ipAddress=ui->le_ip->text();
QString port=ui->le_port->text();
qTcpSocket->connectToHost(ipAddress,port.toInt());
qInfo()<<"ip:"+ipAddress+",port:"+port;
}

void TcpClient::readMessage()
{
qInfo()<<"read Message";
in.startTransaction();
QString message;
in >> message;
if (!in.commitTransaction()){
    qInfo()<<"Error in datastream";
    return;
}
ui->lbl_message->setText(message);
}

void TcpClient::showError()//QAbstractSocket::SocketError socketError)
{
qInfo()<<"show Error";
/*switch (socketError) {
case 0:
    qInfo()<<"Conexion rechazada";
    break;
case 1:
    qInfo()<<"EL host cerro la conexion";

}*/
}

