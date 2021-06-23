using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ChainOfResponsability
{
    public partial class Form1 : Form
    {

        Paquete p = new Paquete();

        public Form1()
        {
            InitializeComponent();

        }

        private AbstractHandler normal = new NormalHandler();
        private AbstractHandler silver = new SilverHandler();
        private AbstractHandler gold = new GoldHandler();
        private AbstractHandler platinum = new PlatinumHandler();
        

        public Paquete P { get => p; set => p = value; }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

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
        private void button1_Click(object sender, EventArgs e)
        {
            //Cadena de sucesion
            normal.SetSuccessor(silver);
            silver.SetSuccessor(gold);
            gold.SetSuccessor(platinum);

            //Asignar valores
            P.PrecioAPagar = Convert.ToDouble(textBox1.Text);
            P.MillasAcumuladas = Convert.ToDouble(textBox2.Text);
            P.MillasAAcumular = Convert.ToDouble(textBox3.Text);

            //Iniciando la cadena
            normal.ProcessPaquete(P);

            //Devolver los valores 
            textBox4.Text = P.Descuento.ToString();
            textBox5.Text = P.PrecioAPagar.ToString();
            textBox6.Text = P.MillasAAcumular.ToString();
        }
        private void textBox4_TextChanged(object sender, EventArgs e)
        {
           
            
        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {
            
                
            
        }

    }
}
