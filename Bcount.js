var c = "Bettyboughtbitterbutter"
var c1 = "BettyBoughtBitterbutter"
var c2 = "BettyBoughtBitterButter"
var student1 = {
    height : 150 ,
    weight : 70
}
var student2 = {
    height : 156,
    weight : 65 ,
    // age : 21
}

var student3 = {
    height : 150 ,
    weight : 70 ,
    // age : 22
}

var a1 = deepEqual(c , c1)
console.log(a1)
var a2 = deepEqual(c , c2)
console.log(a2)
var a3 = deepEqual(student1 , student2)
console.log(a3)
var a4 = deepEqual(student1, student3)
console.log(a4)



var a = 'e'
var x = countBs(c)
var y = countChar(c,a)


function countBs(c) {
    var n = 0
    for (var i = 0;i < c.length; i++) {
        if (c.charAt(i) === "B") {
            n = n + 1
        }
    }console.log(n)
}

function countChar(c,a) {
    var n = 0
    for (var i = 0;i < c.length;i++) {
        if (c.charAt(i) == a) {
            n = n + 1
        }
    }console.log(n)
}

function deepEqual(a,b) {
    if (typeof a === typeof b) {
        var aobj = Object.getOwnPropertyNames(a);
        var bobj = Object.getOwnPropertyNames(b);

        if (aobj.length != bobj.length) {
            return false
        }

        for (var i = 0; i < aobj.length; i++) {
            var name = aobj[i];


            if (a[name] !== b[name]) {
                return false
            }
        }

        return true
    }

}
