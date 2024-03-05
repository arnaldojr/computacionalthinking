### bubble sort

Dentre os algoritmos de ordenação, o Bubble Sort é sem dúvida um dos mais simples de implementar. Também conhecido como ordenação por trocas ou flutuação, sua simplicidade vem com um custo: uma eficiência geralmente inferior quando comparado a outros métodos de ordenação. A complexidade de tempo do Bubble Sort é O(n²), o que significa que para grandes conjuntos de dados, pode não ser a escolha mais eficiente.

### Funcionamento do Algoritmo

O Bubble Sort trabalha repetidamente passando pela lista a ser ordenada, comparando cada par de elementos adjacentes e trocando-os de posição se estiverem na ordem errada. Esse processo se repete até que nenhuma troca seja necessária, o que indica que a lista está ordenada. O algoritmo recebe esse nome porque os elementos maiores "borbulham" para o final da lista a cada passagem, enquanto os menores "afundam" para o início.


![](https://panda.ime.usp.br/panda/static/pythonds_pt/_images/bubblepass.png)


### Implementação em Python

Aqui está uma implementação simples do Bubble Sort em Python:

```python 

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] ## troca de posição
    return lista

```

Neste caso, como exemplo:

```python

lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubble_sort(lista)
print("Lista Ordenada:", lista_ordenada)

```


!!! progress
    continuar...


    
<div id="bubble_anim">
<canvas id="bubble_anim_canvas" width="400" height="400" style="border:4px solid blue"></canvas>
<br>
<button onclick="bubble_anim_anim = bubble_anim_init('bubble_anim')">Initialize</button>
<button onclick="bubble_anim_anim.run('bubble_anim_anim')">Run</button>
<button onclick="bubble_anim_anim.stop()">Stop</button> <br>
<button onclick="bubble_anim_anim.begin()">Beginning</button>
<button onclick="bubble_anim_anim.forward()">Step Forward</button>
<button onclick="bubble_anim_anim.backward()">Step Backward</button>
<button onclick="bubble_anim_anim.end()">End</button>

<script type="text/javascript">
bubble_anim_init = function(divid)
{
   var a = new Animator(new BubbleSortModel(), new BarViewer(), divid)
   a.init()
   return a
}
</script>

</div>