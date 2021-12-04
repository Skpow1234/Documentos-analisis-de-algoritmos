import java.util.Random;
public class DivideyVencerasModa {
	public static void main (String [] args) {
		System.out.println ("Busqueda de la moda en un vector de N elementos.\n");
		System.out.println ("Aplicando tecnicas de divide y venceras.\n");
		System.out.println ("================================================================\n");	
		int N = 1000;										//Define el tamaño del vector
		int [] elVector = new int [N]; 					//elVector es un arreglo de N elementos de tipo enteros
		cargarVector(elVector);							//Cargamos el vector con valores aleatorios
		imprimirVector(elVector);						//Imprimimos los valores del vector
		/*Llamamos al metodo hallarModa e imprimimos el valor devuelto*/
		System.out.println ("\n\nEl valor que mas se repite es: " + hallarModa (elVector, 0 , elVector.length-1));
	}

	/**
	 * Metodo para hallar la moda en un vector de enteros
	 * Utilizando la tecnica Divide y Venceras
	 * @param a
	 * @param prim
	 * @param ult
	 * @return
	 */
	public static int hallarModa (int a[], int prim, int ult) {
		int i, frec, maxfrec, moda;
		if (prim == ult) return a[prim];
		moda = a[prim];
		maxfrec = Frecuencia(a, a[prim], prim, ult);
		for (i = prim + 1; i<=ult; i++) {
			frec = Frecuencia (a, a[i], i, ult);
			if (frec > maxfrec) {
				maxfrec = frec;
				moda = a[i];
			}
		}
		return moda;
	}

	/**
	 * Metodo para calcular el numero de veces que se repite un elemento
	 * Utilizado por el metodo hallarModa
	 * @param a
	 * @param p
	 * @param prim
	 * @param ult
	 * @return
	 */
	public static int Frecuencia (int a[], int p, int prim, int ult) {
		int i, suma;
		if (prim > ult) return 0;
		suma = 0;
		for (i = prim; i<= ult; i++)
			if(a[i] == p)
				suma++;
		return suma;
	}

	/**
	 * Metodo para cargar el vector con valores int aleatorios
	 * @param a
	 */
	public static void cargarVector (int a[]) {
		Random r = new Random();						//Variable para el numero generado aleatoriamente
		for (int i = 0; i< a.length; i++){		//Cargamos el vector con valores aleatorios
			a [i] = (r.nextInt(100));   		//Genera y carga valores aleatorios en elVector
		}
	}
	/**
	 * Metodo para imprimir el vector
	 * @param a
	 */
	public static void imprimirVector (int a[]) {
		System.out.println("\nEl vector es:");
		for (int i = 0; i < a.length; i++) {
			System.out.printf( "%d " , (a[i]) );
		}
	}
}