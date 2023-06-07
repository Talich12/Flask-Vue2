import type { PlayerVars } from '@vue-youtube/shared';
import type { DefineComponent, VNode, RendererNode, RendererElement, ComponentOptionsMixin, VNodeProps, AllowedComponentProps, ComponentCustomProps, ExtractPropTypes, PropType } from 'vue-demi';
export declare const YoutubeIframe: DefineComponent<{
    width: {
        type: PropType<string | number>;
        default: number;
    };
    height: {
        type: PropType<string | number>;
        default: number;
    };
    playerVars: {
        type: PropType<PlayerVars>;
        default: () => {
            autoplay: number;
            time: number;
            mute: number;
        };
    };
    videoId: {
        type: PropType<string>;
        default: string;
    };
    cookie: {
        type: PropType<boolean>;
        default: boolean;
    };
}, () => VNode<RendererNode, RendererElement, {
    [key: string]: any;
}>, unknown, {}, {}, ComponentOptionsMixin, ComponentOptionsMixin, ("playback-quality-change" | "playback-rate-change" | "state-change" | "api-change" | "error" | "ready")[], "playback-quality-change" | "playback-rate-change" | "state-change" | "api-change" | "error" | "ready", VNodeProps & AllowedComponentProps & ComponentCustomProps, Readonly<ExtractPropTypes<{
    width: {
        type: PropType<string | number>;
        default: number;
    };
    height: {
        type: PropType<string | number>;
        default: number;
    };
    playerVars: {
        type: PropType<PlayerVars>;
        default: () => {
            autoplay: number;
            time: number;
            mute: number;
        };
    };
    videoId: {
        type: PropType<string>;
        default: string;
    };
    cookie: {
        type: PropType<boolean>;
        default: boolean;
    };
}>> & {
    "onPlayback-quality-change"?: ((...args: any[]) => any) | undefined;
    "onPlayback-rate-change"?: ((...args: any[]) => any) | undefined;
    "onState-change"?: ((...args: any[]) => any) | undefined;
    "onApi-change"?: ((...args: any[]) => any) | undefined;
    onError?: ((...args: any[]) => any) | undefined;
    onReady?: ((...args: any[]) => any) | undefined;
}, {
    width: string | number;
    height: string | number;
    playerVars: PlayerVars;
    videoId: string;
    cookie: boolean;
}>;
export * from '@vue-youtube/shared';
