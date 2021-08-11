using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ChainOfRespon_Server
{
    public partial class Form1 : Form
    {
        Pedido p;
        public Form1()
        {
            InitializeComponent();
        }

        private AbstractHandler serv1 = new SERV1();
        private AbstractHandler serv2 = new SERV2();
        private AbstractHandler serv3 = new SERV3();
        private AbstractHandler serv4 = new SERV4();
        private AbstractHandler serv5 = new SERV5();
        

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            p = new Pedido();
            //Cadena de sucesion
            serv1.SetSuccessor(serv2);
            serv2.SetSuccessor(serv3);
            serv3.SetSuccessor(serv4);
            serv4.SetSuccessor(serv5);
            serv5.SetSuccessor(serv1);

            //Iniciar cadena
            serv1.servirPedido(p);

            //Devolver los valores
            textBox1.Text=p.Log.ToString();

        }
    }
}
