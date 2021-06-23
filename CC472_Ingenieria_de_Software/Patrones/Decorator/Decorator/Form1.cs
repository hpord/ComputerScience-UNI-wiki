using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Decorator
{
    public partial class Form1 : Form
    {
        Pizza p;

        public Form1()
        {
            InitializeComponent();

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            
        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if(radioButton1.Checked == true)
            {
               p = new BaseJamon();
            }

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if(radioButton2.Checked == true)
            {
               p = new Vegana();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                p=new Queso(p);
            }
            if(checkBox2.Checked)
            {
                p = new Jalapeno(p);
            }
            if(checkBox3.Checked)
            {
                p = new Champi(p);
            }
            if (checkBox4.Checked)
            {
                p = new Tocino(p);
            }

            textBox1.Text=p.precio().ToString();
            
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
           
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            
        }
    }
}
