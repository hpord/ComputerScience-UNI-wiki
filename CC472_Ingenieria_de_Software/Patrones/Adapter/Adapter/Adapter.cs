using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Adapter
{
    public abstract class Triangulo
    {
        int[] array1 = new int[6];
        public abstract bool Display();
      
    }

    public class TipoTriangulo : Triangulo
    {
        private int[] list;
        private bool ifTriangle;
        private triangleUtil verif;

        //Constructor
        public TipoTriangulo(int[] list)
        {
            this.list = list;
        }

        public override bool Display()
        {
            verif = new triangleUtil();
            ifTriangle = verif.Exists(list);
            if (ifTriangle)
            {
                return true;
            }
            else { return false;}
        }


    }



    public class triangleUtil
    {
        public bool Exists(int[] a)
        {
            //float area = p1_x * (p2_y - p3_y) + p2_x * (p3_y - p1_y) + p3_x * (p1_y - p2_y);
            int area = a[0] * (a[3] - a[5]) +
                a[2] * (a[5] - a[1]) +
                a[4] * (a[1] - a[3]);
            if (area == 0)
            {
                return false;
            }
            else
            {
               return true;
                
                }
        
        }
    }
}
