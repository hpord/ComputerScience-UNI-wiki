using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Singleton
{
    public partial class Form1 : Form
    {
        public class Singleton
        {
            private readonly static Singleton _instance = new Singleton();

            private Singleton()
            {

            }

            public static Singleton Instance
            {
                get
                {
                    return _instance;
                }
            }

            public string ultimoInicio="";
            public string ultimoCierre="";
            public int contadorSesiones=0;

            public void IniciarSesion()
            {
                ultimoInicio = DateTime.UtcNow.ToLocalTime().ToString();
            }

            public void CerrarSesion()
            {
                
                if (contadorSesiones > 0)
                {
                    ultimoCierre = DateTime.UtcNow.ToLocalTime().ToString();
                }
            }

            public void AumentarSesion()
            {
                contadorSesiones++;
                
            }

            public void DisminuirSesion()
            {
                contadorSesiones--;
                if(contadorSesiones<0)
                {
                    contadorSesiones = 0;
                }
            }


        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Singleton.Instance.IniciarSesion();
            Singleton.Instance.AumentarSesion();
            textBox1.Text = Singleton.Instance.contadorSesiones.ToString();
            textBox2.Text = Singleton.Instance.ultimoInicio.ToString();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Singleton.Instance.CerrarSesion();
            Singleton.Instance.DisminuirSesion();
            textBox1.Text = Singleton.Instance.contadorSesiones.ToString();
            textBox3.Text = Singleton.Instance.ultimoCierre.ToString();
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
