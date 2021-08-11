using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PatronIterator
{
    public partial class Form1 : Form
    {
        Iterator i;
        private int enter = 0;
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            i = new Iterator(listBox1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Text = i.top();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = i.fin();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Text = i.centro();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Text = i.siguiente();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            textBox1.Text = i.anterior();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if(enter == 0)
            {
                i.labt = 4;
                enter = 1;
            }
            else
            {
                i.labt = 6;
                enter = 0;
            }
        }
    }
}
