<template>
  <div class="relative p-4 board" ref="board">
    <BorderBox1 color="['gray', 'white']">
      <div class="w-full h-full top-10 left-20 absolute tp" ref="panel"></div>
      <div
        class="w-50 h-64 top-20 left-12 absolute p-4 flex-y-start"
      >
        <DvButton
          border="Border3"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          color="#ff9999"
          pad="20,20,20,20"
          @click=put_flow()
        >
          下发硬超时流表
        </DvButton>
        <DvButton
          border="Border3"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          color="#ff9999"
          @click=del_flow()
        >
          删除流表项
        </DvButton>
        <DvButton
          border="Border3"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          color="#ff9999"
          @click=cnt_flow()
        >
        获取流表数量
        </DvButton>
        
        
      </div>

      <div
        class="w-20 h-30 bottom-20 left-12 absolute newtopo"
      >
        <DvButton
          border="Border3"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          color="#ff9999"
          @click=create_topo()
        >
        构建拓扑+启动ODL
        </DvButton>
        
        <div class="flex items-center gap-4 mt-6">
          <p class="font-bold" style="letter-spacing: 0.1em; font-size: 16px">
            设置vlan
          </p>
          <NSwitch v-model:value="isServer" @click=set_vlan></NSwitch>
        </div>

        <DvButton
          border="Border3"
          class="text-center h-10 font-semibold pt-1 w-52"
          fontSize="18px"
          fontColor="#ffffff"
          color="#ff9999"
          @click=test_pingall()
        >
        构建拓扑+启动Ryu
        </DvButton>
      </div>

      <div
        class="border border-blue bottom-8 right-20 absolute p-4"
      >
        <div class="flexr items-center justify-start">
          <span class="w-32">输出内容:</span>
          <p class="mypa" style="font-size:20px">{{ networkData.flowtable_text }}</p>
        </div>
      </div>
    </BorderBox1>
  </div>
</template>

<script setup>
import axios from 'axios';
import { Network } from "vis-network";
import { nextTick, onMounted, ref, watch, reactive } from "vue";
import { useRouter } from "vue-router";
import switchImageUrl from "../assets/Switch.png";
import clientImageUrl from "../assets/Laptop1.png";
import greenclientImageUrl from "../assets/greenlaptop.png";
import orangeclientImageUrl from "../assets/orangelaptop.png";
import switchImageUrl2 from "../assets/Server.png";
import { BorderBox1} from "@kjgl77/datav-vue3";
import { Button as DvButton } from "@kjgl77/datav-vue3";
import { useElementSize } from "@vueuse/core";
import { useGlobalState } from "@/store";
import { NUpload, NSwitch, NButton } from "naive-ui";
import { before, toPairs } from "lodash-es";
var is_topo = false;
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
  flowtable_num: "",
  flowtable_text: "",
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
function put_flow () {
  networkData.flowtable_text = "PUT hardtime flow table OK!";
  axios.get('http://127.0.0.1:5000/put')
  .then(response => {
    networkData.flowtable_text = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function del_flow () {
  networkData.flowtable_text = "delete ok!";
  axios.get('http://127.0.0.1:5000/del')
  .then(response => {
    networkData.flowtable_text = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function cnt_flow () {
  networkData.flowtable_text = "cnt ok!";
  axios.get('http://127.0.0.1:5000/cnt')
  .then(response => {
    networkData.flowtable_text = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function set_vlan () {
  networkData.flowtable_text = "set vlan ok!";
  axios.get('http://127.0.0.1:5000/vlan')
  .then(response => {
    networkData.flowtable_text = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function test_pingall () {
  networkData.flowtable_text = "start ryu and topo ok!";
  axios.get('http://127.0.0.1:5000/pall')
  .then(response => {
    networkData.flowtable_text = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function create_topo () {
  axios.get('http://127.0.0.1:5000/create_topo')
  .then(response => {
    networkData.flowtable_text = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
  networkData.flowtable_text = "create ODL and topo OK!";
}
</script>



<style scoped>
.mypa {
  width: 800px;
  height:1100px;
  overflow:scroll;
}
.board {
  background-color: rgb(32, 31, 31);
}
.flex-y-start {
  height:400px;
  width:500px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.newtopo {
  height:400px;
  width:500px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

.tp {
  width:1700px;
  height:1200px;
}
</style>
