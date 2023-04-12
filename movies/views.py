from django.shortcuts import render

kategori_liste = ["macera", "romantik", "dram", "bilim kurgu"]
film_liste = [
    {
    "film_adi": "film 1",
    "aciklama": "film 1 aciklama",
    "resim": "https://picsum.photos/200/300?random=1",
    "anasayfa": True
    },
    {
        "film_adi": "film 2",
        "aciklama": "film 2 aciklama",
        "resim": "https://picsum.photos/200/300?random=2",
        "anasayfa": True
    },
    {
        "film_adi": "film 3",
        "aciklama": "film 3 aciklama",
        "resim": "https://picsum.photos/200/300?random=3",
        "anasayfa": False
    },
    {
        "film_adi": "film 4",
        "aciklama": "film 4 aciklama",
        "resim": "https://picsum.photos/200/300?random=4",
        "anasayfa": False
    }
]

def home(request): 
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request,"index.html", data)

def movies(request): 
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request,"movies.html", data)
