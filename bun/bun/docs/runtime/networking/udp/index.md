---
title: "UDP"
source: "https://bun.com/docs/runtime/networking/udp"
canonical_url: "https://bun.com/docs/runtime/networking/udp"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:57.828Z"
content_hash: "fd7a7c9f2a2db962e715b901ad39fcab36d406e924637b53d088df6591596439"
menu_path: ["UDP"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/networking/tcp/index.md", "title": "TCP"}
nav_next: {"path": "bun/bun/docs/runtime/node-api/index.md", "title": "Node-API"}
---

## Bind a UDP socket (`Bun.udpSocket()`)

To create a new (bound) UDP socket:

```
const socket = await Bun.udpSocket({});
console.log(socket.port); // assigned by the operating system
```

Specify a port:

```
const socket = await Bun.udpSocket({
  port: 41234, 
});

console.log(socket.port); // 41234
```

### Send a datagram

Specify the data to send, as well as the destination port and address.

```
socket.send("Hello, world!", 41234, "127.0.0.1");
```

Note that the address must be a valid IP address - `send` does not perform DNS resolution, as it is intended for low-latency operations.

### Receive datagrams

When creating your socket, add a callback to specify what should be done when packets are received:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = await Bun.udpSocket({
  socket: {
    data(socket, buf, port, addr) {
      console.log(`message from ${addr}:${port}:`);
      console.log(buf.toString());
    },
  },
});

const client = await Bun.udpSocket({});
client.send("Hello!", server.port, "127.0.0.1");
```

### Connections

While UDP does not have a concept of a connection, many UDP communications (especially as a client) involve only one peer. In such cases it can be beneficial to connect the socket to that peer, which specifies to which address all packets are sent and restricts incoming packets to that peer only.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = await Bun.udpSocket({
  socket: {
    data(socket, buf, port, addr) {
      console.log(`message from ${addr}:${port}:`);
      console.log(buf.toString());
    },
  },
});

const client = await Bun.udpSocket({
  connect: {
    port: server.port,
    hostname: "127.0.0.1",
  },
});

client.send("Hello");
```

Because connections are implemented on the operating system level, you can potentially observe performance benefits, too.

### Send many packets at once using `sendMany()`

If you want to send a large volume of packets at once, it can make sense to batch them all together to avoid the overhead of making a system call for each. This is made possible by the `sendMany()` API: For an unconnected socket, `sendMany` takes an array as its only argument. Each set of three array elements describes a packet: The first item is the data to be sent, the second is the target port, and the last is the target address.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const socket = await Bun.udpSocket({});

// sends 'Hello' to 127.0.0.1:41234, and 'foo' to 1.1.1.1:53 in a single operation
socket.sendMany(["Hello", 41234, "127.0.0.1", "foo", 53, "1.1.1.1"]);
```

With a connected socket, `sendMany` takes an array, where each element represents the data to be sent to the peer.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const socket = await Bun.udpSocket({
  connect: {
    port: 41234,
    hostname: "localhost",
  },
});

socket.sendMany(["foo", "bar", "baz"]);
```

`sendMany` returns the number of packets that were successfully sent. As with `send`, `sendMany` only takes valid IP addresses as destinations, as it does not perform DNS resolution.

### Handle backpressure

It may happen that a packet that you’re sending does not fit into the operating system’s packet buffer. You can detect that this has happened when:

*   `send` returns `false`
*   `sendMany` returns a number smaller than the number of packets you specified. In this case, the `drain` socket handler will be called once the socket becomes writable again:

```
const socket = await Bun.udpSocket({
  socket: {
    drain(socket) {
      // continue sending data
    },
  },
});
```

### Socket options

UDP sockets support setting various socket options:

```
const socket = await Bun.udpSocket({});

// Enable broadcasting to send packets to a broadcast address
socket.setBroadcast(true);

// Set the IP TTL (time to live) for outgoing packets
socket.setTTL(64);
```

### Multicast

Bun supports multicast operations for UDP sockets. Use `addMembership` and `dropMembership` to join and leave multicast groups:

```
const socket = await Bun.udpSocket({});

// Join a multicast group
socket.addMembership("224.0.0.1");

// Join with a specific interface
socket.addMembership("224.0.0.1", "192.168.1.100");

// Leave a multicast group
socket.dropMembership("224.0.0.1");
```

Additional multicast options:

```
// Set TTL for multicast packets (number of network hops)
socket.setMulticastTTL(2);

// Control whether multicast packets loop back to the local socket
socket.setMulticastLoopback(true);

// Specify which interface to use for outgoing multicast packets
socket.setMulticastInterface("192.168.1.100");
```

For source-specific multicast (SSM), use `addSourceSpecificMembership` and `dropSourceSpecificMembership`:

```
socket.addSourceSpecificMembership("10.0.0.1", "232.0.0.1");
socket.dropSourceSpecificMembership("10.0.0.1", "232.0.0.1");
```


