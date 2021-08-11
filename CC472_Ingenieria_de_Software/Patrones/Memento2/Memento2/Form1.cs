using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Memento2
{
    public partial class Form1 : Form
    {
        private Guardian g;
        public Form1()
        {
            InitializeComponent();
        }
        private Memento getMemento()
        {
            return new Memento(label1.ForeColor, label1.Text);
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            g=new Guardian();
            label1.Text = "Rojo";
            label1.ForeColor = Color.Red;
            groupBox1.BackColor= Color.Red;
            g.push(getMemento());
        }


        private void groupBox1_Enter(object sender, EventArgs e)
        {
            
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            g.push(getMemento());
            label1.Text = "Rojo";
            label1.ForeColor = Color.Red;
            groupBox1.BackColor = Color.Red;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            g.push(getMemento());
            label1.Text = "Verde";
            label1.ForeColor = Color.Green;
            groupBox1.BackColor = Color.Green;
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            g.push(getMemento());
            label1.Text = "Azul";
            label1.ForeColor = Color.Blue;
            groupBox1.BackColor = Color.Blue;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Memento m = g.pop();

            label1.Text = m.Texto;
            label1.ForeColor = m.Color;
            groupBox1.BackColor = m.Color;
        }

     

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
