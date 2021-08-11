using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Factoy_Method
{
   abstract class item
    {

    }

    class hotel : item { } 
    
    class auto : item { }
   
    class pasaje: item { }
    
    class pasajeM : item { }
    

    abstract class Paquete
    {
        private List<item> _items = new List<item>();

        public Paquete()
        {
            this.CreatePaquete();
        }

        public List<item> Items
        {
            get { return _items; }
        }

        public abstract void CreatePaquete();
    }


    class PAlto : Paquete
    {
        public override void CreatePaquete()
        {
            Items.Add(new hotelA());
            Items.Add(new autoA());
            Items.Add(new pasajeA());
            Items.Add(new pasajeMA());
        }
    }

    class PBajo : Paquete
    {
        public override void CreatePaquete()
        {
            Items.Add(new hotelB());
            Items.Add(new autoB());
            Items.Add(new pasajeB());
            Items.Add(new pasajeMB());
        }
    }




}
