using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainOfRespon_Server
{
    public class Pedido
    {

        int intentos = 0;
        string log;

        public Pedido()
        {
        }

        public Pedido(int intentos, string log)
        {
            this.intentos = intentos;
            this.Log = log;
        }

        public int Intentos { get => intentos; set => intentos = value; }
        public string Log { get => log; set => log = value; }
        ~Pedido()
        {

        }
    }

    public abstract class AbstractHandler
    {
        protected AbstractHandler successor;
        public void SetSuccessor(AbstractHandler successor)
        {
            this.successor = successor;
        }
        public abstract void servirPedido(Pedido pedido);
    }

    public class SERV1 : AbstractHandler
    {
        public override void servirPedido(Pedido pedido)
        {
            Random r = new Random();
            int cargaActual = r.Next(0, 100);
            if (cargaActual <= 50 && pedido.Intentos < 26)
            {
                pedido.Log = "Servidor 1 | Estado actual del servidor :" + cargaActual + "% | " + "Serv1" + " Intentos : " + pedido.Intentos;
            }

            else
            {
                if (pedido.Intentos > 26)
                {
                    pedido.Log = "No se puede | Estado actual del servidor :" + cargaActual + "% | " + "Serv1" + " Intentos : " + pedido.Intentos;

                }
                else if (successor != null)
                {
                    pedido.Intentos++;
                    successor.servirPedido(pedido);
                }
            }

        }
    }
    public class SERV2 : AbstractHandler
    {
        public override void servirPedido(Pedido pedido)
        {
            Random r = new Random();
            int cargaActual = r.Next(0, 100);
            if (cargaActual <= 50 && pedido.Intentos < 26)
            {
                pedido.Log = "Servidor 2 | Estado actual del servidor :" + cargaActual + "% | " + "Serv2" + " Intentos : " + pedido.Intentos;
            }

            else
            {
                if (pedido.Intentos >= 26)
                {
                    pedido.Log = "No se puede | Estado actual del servidor :" + cargaActual + "% | " + "Serv2" + " Intentos : " + pedido.Intentos;

                }
                else if (successor != null)
                {
                    pedido.Intentos++;
                    successor.servirPedido(pedido);
                }
            }

        }
    }
    public class SERV3 : AbstractHandler
    {
        public override void servirPedido(Pedido pedido)
        {
            Random r = new Random();
            int cargaActual = r.Next(0, 100);
            if (cargaActual <= 50 && pedido.Intentos < 26)
            {
                pedido.Log = "Servidor 3 | Estado actual del servidor :" + cargaActual + "% | " + "Serv3" + " Intentos : " + pedido.Intentos;
            }

            else
            {
                if (pedido.Intentos >= 26)
                {
                    pedido.Log = "No se puede | Estado actual del servidor :" + cargaActual + "% | " + "Serv3" + " Intentos : " + pedido.Intentos;

                }
                else if (successor != null)
                {
                    pedido.Intentos++;
                    successor.servirPedido(pedido);
                }
            }

        }
    }
    public class SERV4 : AbstractHandler
    {
        public override void servirPedido(Pedido pedido)
        {
            Random r = new Random();
            int cargaActual = r.Next(0, 100);


            if (cargaActual <= 50 && pedido.Intentos < 26)
            {
                pedido.Log = "Servidor 4 | Estado actual del servidor :" + cargaActual + "% | " + "Serv4" + " Intentos : " + pedido.Intentos;
            }

            else
            {
                if (pedido.Intentos >= 26)
                {
                    pedido.Log = "No se puede | Estado actual del servidor :" + cargaActual + "% | " + "Serv4" + " Intentos : " + pedido.Intentos;

                }
                else if (successor != null)
                {
                    pedido.Intentos++;
                    successor.servirPedido(pedido);
                }
            }

        }
    }

    public class SERV5 : AbstractHandler
    {
        public override void servirPedido(Pedido pedido)
        {
            Random r = new Random();
            int cargaActual = r.Next(0, 100);
            if (cargaActual <= 50 && pedido.Intentos < 26)
            {
                pedido.Log = "Servidor 5 | Estado actual del servidor :" + cargaActual + "% | " + "Serv5" + " Intentos : " + pedido.Intentos;
            }

            else
            {
                if (pedido.Intentos >= 26)
                {
                    pedido.Log = "No se puede | Estado actual del servidor :" + cargaActual + "% | " + "Serv5" + " Intentos : " + pedido.Intentos;

                }
                else if (successor != null)
                {
                    pedido.Intentos++;
                    successor.servirPedido(pedido);
                }
            }
        }
    }
}
