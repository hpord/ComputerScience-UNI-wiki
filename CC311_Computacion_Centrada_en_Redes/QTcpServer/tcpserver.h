#ifndef TCPSERVER_H
#define TCPSERVER_H

#include <QDialog>
#include <QTcpServer>
QT_BEGIN_NAMESPACE
namespace Ui { class tcpserver; }
QT_END_NAMESPACE

class TcpServer : public QDialog
{
    Q_OBJECT

public:
    TcpServer(QWidget *parent = nullptr);
    ~TcpServer();

private:
    Ui::tcpserver *ui;
    QTcpServer *QTcpServer = nullptr;
    QVector<QString> randomMessages;

void initServer();
private slots:
    void sendRandomMessage();
};
#endif // TCPSERVER_H
