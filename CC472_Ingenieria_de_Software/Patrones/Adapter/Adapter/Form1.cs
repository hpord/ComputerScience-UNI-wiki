using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Adapter
{
    public partial class Form1 : Form
    {
        int Min = -10;
        int Max = 10;
        bool state;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Triangulo t;

            Random randNum = new Random();
            int[] list = Enumerable.Repeat(0, 6).Select(i => randNum.Next(Min, Max))
            .ToArray();
            textBox1.Text = list[0].ToString();
            textBox2.Text = list[1].ToString();
            textBox3.Text = list[2].ToString();
            textBox4.Text = list[3].ToString();
            textBox5.Text = list[4].ToString();
            textBox6.Text = list[5].ToString();
            t = new TipoTriangulo(list);
            state = t.Display();

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            label4.Text = state.ToString();
        }
    }
}
