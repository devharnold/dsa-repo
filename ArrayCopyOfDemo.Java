public class ArrayCopyOfDemo {
    public static void main(String[] args) {
        String[] copyFrom = {
            "Affogato", "Americano", "Cappucino", "Correto", "Cortado",
            "Doppio", "Espresso", "Frappucino", "Freddo", "Lungo", "Machiatto",
            "Marocchino", "Ristretto" };
        String[] copyTo = java.util.Arrays.copyOfRange(copyFrom, 2, 9);
        for (String coffee : copyTo) {
            System.out.println(coffee + " ");
        }
    }
}