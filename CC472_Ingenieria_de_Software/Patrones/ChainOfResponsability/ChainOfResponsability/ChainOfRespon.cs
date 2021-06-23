using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainOfResponsability
{
    public class Paquete {

        double descuento;
        double millasAAcumular;
        double precioAPagar;
        double millasAcumuladas;

        public Paquete()
        {
        }

        public Paquete(double descuento, double millasAAcumular, double precioAPagar, double millasAcumuladas)
        {
            this.Descuento = descuento;
            this.MillasAAcumular = millasAAcumular;
            this.PrecioAPagar = precioAPagar;
            this.MillasAcumuladas = millasAcumuladas;
        }

        public double Descuento { get => descuento; set => descuento = value; }
        public double MillasAAcumular { get => millasAAcumular; set => millasAAcumular = value; }
        public double PrecioAPagar { get => precioAPagar; set => precioAPagar = value; }
        public double MillasAcumuladas { get => millasAcumuladas; set => millasAcumuladas = value; }
    }
    public abstract class AbstractHandler
    {
        protected AbstractHandler successor;
        public void SetSuccessor(AbstractHandler successor)
        {
            this.successor = successor;
        }
        public abstract void ProcessPaquete(Paquete paquete);
    }

    public class NormalHandler : AbstractHandler
    {
        public override void ProcessPaquete(Paquete paquete)
        {
            if ( paquete.MillasAcumuladas < 10000)
            {
                paquete.Descuento = 0;
                paquete.PrecioAPagar = paquete.PrecioAPagar - (paquete.PrecioAPagar * (paquete.Descuento / 100));
                paquete.MillasAcumuladas += (paquete.MillasAAcumular * 1);
                paquete.MillasAAcumular = paquete.MillasAAcumular * 1;
            }
            else if (successor != null)
            {
                successor.ProcessPaquete(paquete);
            }
        }
    }

    public class SilverHandler : AbstractHandler
    {
        public override void ProcessPaquete(Paquete paquete)
        {
            if(paquete.MillasAcumuladas>10001 && paquete.MillasAcumuladas < 25000)
            {
                paquete.Descuento = 5;
                paquete.PrecioAPagar = paquete.PrecioAPagar-(paquete.PrecioAPagar*(paquete.Descuento/100));
                paquete.MillasAcumuladas += (paquete.MillasAAcumular * 1.1);
                paquete.MillasAAcumular = paquete.MillasAAcumular * 1.1;
            }
            else if (successor != null)
            {
                successor.ProcessPaquete(paquete);
            }
        }
    }

    public class GoldHandler : AbstractHandler
    {
        public override void ProcessPaquete(Paquete paquete)
        {
            if (paquete.MillasAcumuladas > 25001 && paquete.MillasAcumuladas < 50000)
            {
                paquete.Descuento = 10;
                paquete.PrecioAPagar = paquete.PrecioAPagar - (paquete.PrecioAPagar * (paquete.Descuento / 100));
                paquete.MillasAcumuladas += (paquete.MillasAAcumular * 2);
                paquete.MillasAAcumular = paquete.MillasAAcumular * 2;
            }
            else if (successor != null)
            {
                successor.ProcessPaquete(paquete);
            }
        }
    }
    public class PlatinumHandler : AbstractHandler
    {
        public override void ProcessPaquete(Paquete paquete)
        {
            if (paquete.MillasAcumuladas > 50000)
            {
                paquete.Descuento = 20;
                paquete.PrecioAPagar = paquete.PrecioAPagar - (paquete.PrecioAPagar * (paquete.Descuento / 100));
                paquete.MillasAcumuladas += (paquete.MillasAAcumular * 3);
                paquete.MillasAAcumular = paquete.MillasAAcumular * 3;
            }
            
        }
    }


}
