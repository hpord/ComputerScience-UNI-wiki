using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Decorator
{

    public abstract class Pizza
    {
        public abstract double precio();
        ~Pizza() { }
    }
    public class BaseJamon : Pizza
    {
        public override double precio()
        {
            return 10.0;
        }
        
    }
    public class Vegana : Pizza
    {

        public override double precio()
        {
            return 6.0;
        }

       
    }
    public abstract class AbstractDecorator : Pizza
    {
        protected Pizza miDecorado;

    }

    public class Queso : AbstractDecorator
    {
        public Queso(Pizza p)
        {
            miDecorado = p;
        }

        public override double precio()
        {
            return 5 + miDecorado.precio();
        }
    }

    public class Jalapeno : AbstractDecorator
    {
        public Jalapeno(Pizza p)
        {
            miDecorado = p;
        }

        public override double precio()
        {
            return 3 + miDecorado.precio();
        }
    }
    public class Champi : AbstractDecorator
    {
        public Champi(Pizza p)
        {
            miDecorado = p;
        }

        public override double precio()
        {
            return 4 + miDecorado.precio();
        }
    }

    public class Tocino : AbstractDecorator
    {
        public Tocino(Pizza p)
        {
            miDecorado = p;
        }

        public override double precio()
        {
            return 2 + miDecorado.precio();
        }


    }
}




        /*
    public abstract class PizzaItem
    {
        private string pizzaType;
        public string PizzaType
        {
            get { return pizzaType; }
            set {pizzaType=value; } 
        }
    }

    public class Pizza : PizzaItem
    {
        private bool queso;
        private bool Jalapeno;
        private bool Champi;
        private bool Tocino;

        public Pizza(bool queso, bool jalapeno, bool champi,bool tocino, string pizzaType)
        {
            this.queso = queso;
            this.Jalapeno = jalapeno;
            this.Champi = champi;
            this.Tocino = tocino;
            this.PizzaType = pizzaType;
        }
    }
    public abstract class Decorator : PizzaItem
    {
        protected PizzaItem pizzaItem;
        //Constructor
        public Decorator(PizzaItem pizzaItem)
        {
            this.pizzaItem = pizzaItem;
        }
    }
    public class Calculator : Decorator
    {
        int price;

    }
        */









    
