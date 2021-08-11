using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Factoy_Method
{
    public partial class Form1 : Form
    {
        Paquete p;
        

        public Form1()
        {
            InitializeComponent();
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string[] m = new string[3];
           
          
            var result = dateTimePicker1.Value.Month;
            if ((result>=7 && result<= 8)|(result>=3 && result<=12))
            {
                p = new PAlto();
                foreach(item i in p.Items)
                {
                    m.Append(i.GetType().Name);
                }

            }
            else
            {
                p=new PBajo();
                foreach (item i in p.Items)
                {
                    m.Append(i.GetType().Name);
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
