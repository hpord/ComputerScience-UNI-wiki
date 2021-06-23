using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Iterator
{
  public class Item
    {

        string name;

        public Item(string name)
        {
            this.Name = name;
        }

        public string Name { get => name; set => name = value; }
    }




    public interface IAbstractIterator
    {
       
    }

    public class Iterator : IAbstractIterator
    {
       
    }

}
