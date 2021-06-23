using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Memento2
{
    public class Memento
    {

        Color color;
        string texto;

        public Memento(Color color, string texto)
        {
            this.Color = color;
            this.Texto = texto;
        }

        public Color Color { get => color; set => color = value; }
        public string Texto { get => texto; set => texto = value; }
    }

    public class Guardian
    {
        private Stack<Memento> mementos = new Stack<Memento>();
        public void push(Memento m)
        {
            mementos.Push(m);
        }
        public Memento pop()
        {
            return mementos.Pop();
        }

    }


}
