#include "tcpserver.h"
#include "ui_tcpserver.h"

TcpServer::TcpServer(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::tcpserver)
{
    ui->setupUi(this);
    //mensajes aleatorios
    for(int i=0;i<20;i++){
        randomMessages<<"Mensaje aleatorio"+QString::number(i);
    }
    //conexiones
    connect(ui->btn_close,QAbstractButton::clicked,this,&QWidget::close);
}

TcpServer::~TcpServer()
{
    delete ui;
}

void TcpServer::initServer(){
    qInfo()<<"init server";

}
void TcpServer::sendRandomMessage(){
    qInfo()<<"Send random message";
}
