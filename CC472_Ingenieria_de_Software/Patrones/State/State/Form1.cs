using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace State
{
    public partial class Form1 : Form
    {
        Puerta p = new Puerta();
        
        
        public Form1()
        {
            InitializeComponent();
           // p.State = new Cerrado(p);
            p.changeState(new Cerrado(p));
            label2.Text = p.getState();
        }

       

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                p.abrir();
            }
            if(radioButton2.Checked == true)
            {
                p.cerrar();
            }
            if(radioButton3.Checked == true)
            {
                p.armar();
            }
            if(radioButton4.Checked == true)
            {
                p.desarmar();
            }
            if(radioButton5.Checked == true)
            {
                p.reparar();
            }
            label2.Text = p.getState();
        }
    }
}
