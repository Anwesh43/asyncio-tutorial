const express = require('express')
const server = express()
server.get('/task/:time',(req,res)=>{
    const time = parseInt(req.params.time || "1")*1000
    setTimeout(()=>{
        res.json({status:"ok"})
    },time)
})
server.listen(8000)
