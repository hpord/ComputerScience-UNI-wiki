using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PatronIterator
{
    public class Iterator
    {
        private ListBox lb;
        private int actual = 0;
        public int labt = 6;

        public Iterator(ListBox L)
        {
            lb = L;
        }

        public String top()
        {
            actual = 0;
            return lb.Items[actual].ToString();
        }
        public String fin()
        {
            actual = labt;
            return lb.Items[actual].ToString();
        }
        public String centro()
        {
            actual = (labt) / 2;
            return lb.Items[actual].ToString();
        }
        public String siguiente()
        {
            
            actual++;
            if (actual > labt)
            {
                actual = 0;
                return lb.Items[actual].ToString();
            }
            return lb.Items[actual].ToString();

        }
        public String anterior()
        {
            actual--;
            if (actual < 0)
            {
                actual = labt;
                return lb.Items[actual].ToString();
            }
            return lb.Items[actual].ToString();
        }
    }
}
