using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DecoratorAvion
{
    public partial class Form1 : Form
    {
        Boleto b;
        
        public Form1()
        {
            InitializeComponent();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void checkBox5_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            b = new BoletoAvion();

            if (checkBox1.Checked)
            {
                b = new Hotel(b);
            }
            if (checkBox2.Checked)
            {
                b=new Automovil(b);
            }
            if (checkBox3.Checked)
            {
                b=new TourInfantil(b);
            }
            if (checkBox4.Checked)
            {
                b=new TourCompras(b);
            }
            if (checkBox5.Checked)
            {
                b=new EntradaD(b);
            }
            if (checkBox6.Checked)
            {
                b = new EntradaU(b);
            }
            if (checkBox7.Checked)
            {
                b= new EntradaM(b);
            }
            textBox1.Text=b.precio().ToString();
        }

        private void checkBox1_CheckedChanged_1(object sender, EventArgs e)
        {

        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }
    }
}
