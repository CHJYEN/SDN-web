<template>
  <div class="relative p-4 board" ref="board">
    <BorderBox1 color="['gray', 'white']" :key="hright">
      <div class="w-full h-full top-10 right-20" ref="panel"></div>
      <div
        class="border border-white w-50 h-100 top-12 left-8 absolute p-4 flex-y-start"
      >
        <DvButton
          border="Border3"
          color="#708090"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          @click="networkData.flowtable_num = 7;networkData.my_out = '这里是硬超时流表项内容';networkData.flowtable_text1 = 'cookie=0x2b00000000000009, duration=7.853s, table=0, n_packets=3, n_bytes=247, priority=2,in_port= s1-eth3  actions=output: s1-eth2 ,output: s1-eth1\
 cookie=0x2b0000000000000b, duration=7.853s, table=0, n_packets=1, n_bytes=70, priority=2,in_port= s1-eth1  actions=output: s1-eth3 ,output: s1-eth2 ,CONTROLLER:65535\
 cookie=0x2b0000000000000a, duration=7.853s, table=0, n_packets=1, n_bytes=70, priority=2,in_port= s1-eth2  actions=output: s1-eth3 ,output: s1-eth1 ,CONTROLLER:65535\
 cookie=0x2b00000000000007, duration=12.149s, table=0, n_packets=24, n_bytes=2897, priority=0 actions=drop';networkData.flowtable_text2 = 'cookie=0x2b00000000000007, duration=7.865s, table=0, n_packets=1, n_bytes=70, priority=2,in_port= s2-eth2  actions=output: s2-eth3 ,output: s2-eth1 ,CONTROLLER:65535\
 cookie=0x2b00000000000008, duration=7.865s, table=0, n_packets=1, n_bytes=70, priority=2,in_port= s2-eth1  actions=output: s2-eth3 ,output: s2-eth2 ,CONTROLLER:65535\
 cookie=0x2b00000000000006, duration=12.202s, table=0, n_packets=21, n_bytes=2647, priority=0 actions=drop'"
        >
          下发硬超时流表
        </DvButton>
        <DvButton
          border="Border3"
          color="#708090"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          @click="networkData.flowtable_num = 0; networkData.flowtable_text1 = '*** s1-------------------------------';networkData.flowtable_text2 = '*** s2-------------------------------'"
        >
          删除流表项
        </DvButton>
        <DvButton
          border="Border3"
          color="#708090"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          @click="networkData.flowtable_num = networkData.flowtable_num==''?2:networkData.flowtable_num"
        >
        获取流表数量
        </DvButton>
        
        <div class="flex items-center gap-4 mt-6">
          <p class="font-bold" style="letter-spacing: 0.1em; font-size: 16px">
            设置vlan
          </p>
          <NSwitch v-model:value="isServer" @click="networkData.flowtable_num = 8;networkData.flowtable_text1 = 'cookie=0x0, duration=710.783s, table=0, n_packets=635, n_bytes=38100, priority=65535,dl_dst=01:80:c2:00:00:0e,dl_type=0x88cc actions=CONTROLLER:65535\
 cookie=0x0, duration=7.174s, table=0, n_packets=0, n_bytes=0, priority=1,in_port= s1-eth1 actions=push_vlan:0x8100,set_field:4096->vlan_vid,output: s1-eth3 \
 cookie=0x0, duration=7.172s, table=0, n_packets=0, n_bytes=0, priority=1,in_port= s1-eth2 actions=push_vlan:0x8100,set_field:4097->vlan_vid,output: s1-eth3 \
 cookie=0x0, duration=7.170s, table=0, n_packets=1, n_bytes=74, priority=1,dl_vlan=0 actions=pop_vlan,output: s1-eth1 \
 cookie=0x0, duration=7.168s, table=0, n_packets=0, n_bytes=0, priority=1,dl_vlan=1 actions=pop_vlan,output: s1-eth2 ';networkData.flowtable_text2 = 'cookie=0x0, duration=710.795s, table=0, n_packets=637, n_bytes=38220, priority=65535,dl_dst=01:80:c2:00:00:0e,dl_type=0x88cc actions=CONTROLLER:65535\
 cookie=0x0, duration=7.178s, table=0, n_packets=1, n_bytes=70, priority=1,in_port= s2-eth1  actions=push_vlan:0x8100,set_field:4096->vlan_vid,output: s2-eth3 \
 cookie=0x0, duration=7.176s, table=0, n_packets=0, n_bytes=0, priority=1,in_port= s2-eth2  actions=push_vlan:0x8100,set_field:4097->vlan_vid,output: s2-eth3 \
 cookie=0x0, duration=7.174s, table=0, n_packets=0, n_bytes=0, priority=1,dl_vlan=0 actions=pop_vlan,output: s2-eth1 '"/>
        </div>

      </div>



      <div
        class="border border-white w-50 h-300 top-8 right-8 absolute p-4"
      >
        <div class="flex items-center justify-start">
          <span class="w-32">流表数量为:</span>
          <p>{{ networkData.flowtable_num }}</p>          
        </div>
        <div class="flexr items-center justify-start">
          <span class="w-32">流表内容:</span>
          <p class="mypa" style="font-size:15px">{{ networkData.flowtable_text1 }}<br>
            -------------------------------------<br>
            {{ networkData.flowtable_text2 }}</p>
        </div>
      </div>
    </BorderBox1>
  </div>
</template>

<script setup>
import { Network } from "vis-network";
import { nextTick, onMounted, ref, watch, reactive } from "vue";
import { useRouter } from "vue-router";
import switchImageUrl from "../assets/Switch.png";
import clientImageUrl from "../assets/sgray.png";
import greenclientImageUrl from "../assets/s1.png";
import orangeclientImageUrl from "../assets/s2.png";
import switchImageUrl2 from "../assets/Server.png";
import { BorderBox1} from "@kjgl77/datav-vue3";
import { Button as DvButton } from "@kjgl77/datav-vue3";
import { useElementSize } from "@vueuse/core";
import { useGlobalState } from "@/store";
import { NUpload, NSwitch, NButton } from "naive-ui";
import { before } from "lodash-es";
const board = ref();
const { width } = useElementSize(board);
const panel = ref();
const { isEase } = useGlobalState();
const isServer = ref(false);
const isWorker = ref(false);
const isLearning = ref(true);
const dbg = "123456465";
const options = {
  nodes: {
    font: {
      color: "#fff",
    },
    color: "#fff",
  },
  edges: {
    color: "rgba(255,255,255,0.2)",
  },
  layout: {
    hierarchical: {
      direction: "LR",
    },
  },
};
const nodes = [
  {
    id: 0,
    label: "h1",
    level: 3,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 2,
    label: "h2",
    level: 3,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 3,
    label: "h3",
    level: 6,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 4,
    label: "h4",
    level: 6,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 5,
    label: "S1",
    level: 4,
    image: switchImageUrl,
    shape: "image",
  },
  {
    id: 6,
    label: "S2",
    level: 5,
    image: switchImageUrl,
    shape: "image",
  },

];
function createDot(hexColor) {
  return {
    enabled: true,
    type: "image",
    imageWidth: 12,
    imageHeight: 12,
    src: `data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' style='width:24px;height:24px' viewBox='0 0 24 24'%3E%3Ccircle cx='12' cy='12' r='10' fill='%23${hexColor.slice(
      1
    )}' /%3E%3C/svg%3E`,
  };
}
const redDot = createDot("#ff0000");
const greenDot = createDot("#00ff00");
const yellowDot = createDot("#EAB308");
const edges = [
  {
    from: 1,
    to: 5,
  },
  {
    from: 2,
    to: 5,
  },
  {
    from: 5,
    to: 6,
  },
  {
    from: 3,
    to: 6,
  },
  {
    from: 4,
    to: 6,
  },
];
const router = useRouter();
function renderNets() {
  // console.log(isServer.value);
  if (isServer.value) {
    nodes[0] = {
      id: 1,
      label: "h1",
      level: 3,
      image: greenclientImageUrl,
      shape: "image",
    };
    nodes[2] = {
      id: 3,
      label: "h3",
      level: 6,
      image: greenclientImageUrl,
      shape: "image",
    };
    nodes[1] = {
      id: 2,
      label: "h2",
      level: 3,
      image: orangeclientImageUrl,
      shape: "image",
    };
    nodes[3] = {
      id: 4,
      label: "h4",
      level: 6,
      image: orangeclientImageUrl,
      shape: "image",
    };
  } else {
    nodes[0] = {
      id: 1,
      label: "h1",
      level: 3,
      image: clientImageUrl,
      shape: "image",
    };
    nodes[2] = {
      id: 3,
      label: "h3",
      level: 6,
      image: clientImageUrl,
      shape: "image",
    };
    nodes[1] = {
      id: 2,
      label: "h2",
      level: 3,
      image: clientImageUrl,
      shape: "image",
    };
    nodes[3] = {
      id: 4,
      label: "h4",
      level: 6,
      image: clientImageUrl,
      shape: "image",
    };
  }
  console.log(nodes[0]);
  new Network(panel.value, { nodes, edges }, options).on(
    "doubleClick",
    function (params) {
      const label = nodes.find((v) => v.id === params.nodes[0]).label;
      if (label.startsWith("h")) router.push(`/flow?label=${label}`);
      // alert(JSON.stringify(params, null, 4))
    }
  );
}
const networkData = reactive({
  flowtable_num: 0,
  flowtable_text1: "*** s1 \
 cookie=0x0, duration=143.343s, table=0, n_packets=5, n_bytes=300, priority=65535, dl_dst=01:80:c2:00:00:0e, dl_type=0x88cc actions=CONTROLLER:65535",
  flowtable_text2:"*** s2 \
 cookie=0x0, duration=143.355s, table=0, n_packets=7, n_bytes=420, priority=65535, dl_dst=01:80:c2:00:00:0e, dl_type=0x88cc actions=CONTROLLER:65535", 
 my_out: "",
});
onMounted(() => {
  renderNets();
});

watch(width, () => {
  nextTick(() => renderNets());
});

watch(isEase, () => {
  if (isEase.value) {
    nextTick(() => {
      setTimeout(() => {
        changeShow2();
        isLearning.value = false;
      }, 5000);
    });
  } else {
    isLearning.value = true;
    networkData.train_loss = "";
    networkData.train_acc = "";
    networkData.val_loss = "";
    networkData.val_acc = "";
  }
});
watch(isLearning, () => {
  if (!isLearning.value) {
    nextTick(() => {
      if (isShow.value) {
        changeShow2();
      } else {
        changeShow1();
      }
    });
  }
});
watch(isServer, () => {
  nextTick(() => {
    renderNets();
  });
});
watch(isWorker, () => {
  nextTick(() => {
    // 改变主机图片
  });
});

const isShow = ref(true);
function changeShow1() {
  isShow.value = false;
  if (!isLearning.value) {
    networkData.train_loss = "0.234";
    networkData.train_acc = "0.989";
    networkData.val_loss = "0.012";
    networkData.val_acc = "0.956";
  }
}
function changeShow2() {
  isShow.value = true;
  if (!isLearning.value) {
    networkData.train_loss = "0.012";
    networkData.train_acc = "0.978";
    networkData.val_loss = "0.234";
    networkData.val_acc = "0.967";
  }
}
const dataFileList = reactive([]);
const codeFileList = reactive([]);

// 文件上传和删除
const beforeUploadData = () => {
  console.log("before upload data");
  return true;
};
const beforeUploadCode = () => {
  console.log("before upload code");
  return true;
};
// const uploadData = (item) => {
//   console.log("item" + item.file);
//   dataFileList.push(item.file);
// };
const uploadFiles = () => {
  // 遍历文件列表，处理每个文件的上传逻辑
  dataFileList.forEach((file) => {
    const reader = new FileReader();

    reader.onload = (event) => {
      // 文件读取成功后的处理逻辑
      const fileData = event.target.result;
      console.log(fileData);
    };

    reader.onerror = (event) => {
      // 文件读取失败的处理逻辑
      console.error("文件读取失败");
    };

    reader.readAsDataURL(file); // 以DataURL的形式读取文件内容
  });
};
const uploadData = ({ file }) => {
  console.log("upload data");
  dataFileList.push(file.file);
};
const uploadCode = (item) => {
  console.log(item);
  codeFileList.push(item.file);
};
const finishData = () => {
  console.log("上传成功data");
};
const finishCode = () => {
  console.log("上传成功code");
};
</script>
<style scoped>
.flex-y-start {
  width: 370px;
  height: 800px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.mypa {
  width: 450px;
  height:800px;
  overflow:scroll;
}
.board {
  background-color: rgb(32, 31, 31);
}
</style>
