using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace State
{

    public abstract class State
    {
        protected Puerta miPuerta;
        public abstract void abrir();
        public abstract void cerrar();
        public abstract void armar();
        public abstract void desarmar();

    public abstract void reparar();
      

    }

    public class Abierto : State
    {
        public Abierto()
        {
        }

        public Abierto(Puerta p) 
        {
            miPuerta = p;
        }

        public override void abrir()
        {
            return;
        }

        public override void armar()
        {
            return;
        }

        public override void cerrar()
        {
            miPuerta.changeState(new Cerrado(miPuerta));
        }

        public override void desarmar()
        {
            return;
        }

        public override void reparar()
        {
            return;
        }
    }

    public class Cerrado : State
    {
        public Cerrado()
        {
        }

        public Cerrado(Puerta p )
        {
            miPuerta = p;
        }

        public override void abrir()
        {
            miPuerta.changeState(new Abierto(miPuerta));
        }

        public override void armar()
        {
            miPuerta.changeState(new Armada(miPuerta));
        }

        public override void cerrar()
        {
            return;
        }

        public override void desarmar()
        {
            return;
        }

        public override void reparar()
        {
            return;
        }
    }

    public class Armada : State
    {
        public Armada()
        {
        }

        public Armada(Puerta p)
        {
            miPuerta = p;
        }

        public override void abrir()
        {
            miPuerta.changeState(new Emergencia(miPuerta));
        }

        public override void armar()
        {
            return;
        }

        public override void cerrar()
        {
            return;
        }

        public override void desarmar()
        {
            miPuerta.changeState(new Cerrado(miPuerta));
        }

        public override void reparar()
        {
            return;
        }
    }

    public class Emergencia : State
    {
        public Emergencia()
        {
        }

        public Emergencia(Puerta p )
        {
            miPuerta = p;
        }

        public override void abrir()
        {
            return;
        }

        public override void armar()
        {
            return;
        }

        public override void cerrar()
        {
            return;
        }

        public override void desarmar()
        {
            return;
        }

        public override void reparar()
        {
            miPuerta.changeState(new Cerrado(miPuerta));
        }
    }

    

    public class Puerta
    {
        private State state;

        public State State { get => state; set => state = value; }

        public  void abrir() { State.abrir();}
        public void cerrar() { State.cerrar();}
        public  void armar() { State.armar();}
        public  void desarmar() { State.desarmar();}
        public void reparar()
        {
            State.reparar();
        }
        public void changeState(State newState)
        {
            State = newState;
        }
        public string getState() {
            return State.ToString(); }



    }




}
