using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecoratorAvion
{
 public abstract class Boleto
    {
        public abstract double precio();

    }
    public class BoletoAvion : Boleto
    {
        public override double precio()
        {
            return 100;
        }
    }

    public abstract class AbstractDecorator : Boleto
    {
        protected Boleto miBoleto;
    }

    public class Hotel : AbstractDecorator
    {
        public Hotel(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return 20+miBoleto.precio();
        }
    }

    public class Automovil : AbstractDecorator
    {
        public Automovil(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return 30 + miBoleto.precio();
        }
    }
    public class TourInfantil: AbstractDecorator
    {
        public TourInfantil(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return miBoleto.precio();
        }
    }
    public class TourCompras : AbstractDecorator
    {
        public TourCompras(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return miBoleto.precio();
        }
    }

    public class EntradaD : AbstractDecorator
    {
        public EntradaD(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return 40 + miBoleto.precio();
        }
    }

    public class EntradaU: AbstractDecorator
    {
        public EntradaU(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return 40 + miBoleto.precio();
        }
    }
    public class EntradaM : AbstractDecorator
    {
        public EntradaM(Boleto b)
        {
            miBoleto = b;
        }

        public override double precio()
        {
            return 40 + miBoleto.precio();
        }
    }




}
