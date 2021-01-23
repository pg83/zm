func NextPermute(_ p: [Int]) -> [Int] {
  if p.count < 2 {
    return []
  }

  var k = -1

  for i in 0..<(p.count - 1) {
    if p[i] < p[i + 1] {
      k = i
    }
  }

  if k < 0 {
    return []
  }

  var l = k + 1

  for i in l..<p.count {
    if p[k] < p[i] {
      l = i
    }
  }

  var pp = p

  let tmp = pp[k]
  pp[k] = pp[l]
  pp[l] = tmp

  pp[(k + 1)..<p.count].reverse()

  return pp
}

func F68() -> String {
  var res = ""

  let lines = [
    [0, 2, 3],
    [1, 3, 7],
    [8, 7, 6],
    [9, 6, 4],
    [5, 4, 2]
  ]

  var p = [Int](1...10)

  while p.count > 0 {
    let x = (0...4).map {
      lines[$0].map {
        p[$0]
      }
    }

    if ((0...4).map{x[0][0] < x[$0][0] ? 1 : 0}.reduce(0, +)) == 4 {
      if Set<Int>(x.map{$0.reduce(0, +)}).count == 1 {
        let ds = x.reduce([], +).map{String($0)}.reduce(String(), +)

        if ds.characters.count == 16 && ds > res {
          res = ds
        }
      }
    }

    p = NextPermute(p)
  }

  return res
}

print(F68())
