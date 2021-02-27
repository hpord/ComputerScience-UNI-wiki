import numpy as np
from numbers import Integral

from sklearn.externals import six
from sklearn.tree.export import _color_brew, _criterion, _tree


def plot_tree(decision_tree, max_depth=None, feature_names=None,
              class_names=None, label='all', filled=False,
              leaves_parallel=False, impurity=True, node_ids=False,
              proportion=False, rotate=False, rounded=False,
              special_characters=False, precision=3, ax=None, fontsize=None):
    """Dibuja un arbol de decision.

    Ejemplos
    --------
    >>> from sklearn.datasets import load_iris

    >>> clf = tree.DecisionTreeClassifier()
    >>> iris = load_iris()

    >>> clf = clf.fit(iris.data, iris.target)
    >>> plot_tree(clf)                

    """
    exporter = _MPLTreeExporter(
        max_depth=max_depth, feature_names=feature_names,
        class_names=class_names, label=label, filled=filled,
        leaves_parallel=leaves_parallel, impurity=impurity, node_ids=node_ids,
        proportion=proportion, rotate=rotate, rounded=rounded,
        special_characters=special_characters, precision=precision,
        fontsize=fontsize)
    exporter.export(decision_tree, ax=ax)


class _BaseTreeExporter(object):
    def get_color(self, value):
        if self.colors['bounds'] is None:
            color = list(self.colors['rgb'][np.argmax(value)])
            sorted_values = sorted(value, reverse=True)
            if len(sorted_values) == 1:
                alpha = 0
            else:
                alpha = ((sorted_values[0] - sorted_values[1])
                         / (1 - sorted_values[1]))
        else:
            color = list(self.colors['rgb'][0])
            alpha = ((value - self.colors['bounds'][0]) /
                     (self.colors['bounds'][1] - self.colors['bounds'][0]))
        alpha = float(alpha)
        color = [int(round(alpha * c + (1 - alpha) * 255, 0)) for c in color]
        hex_codes = [str(i) for i in range(10)]
        hex_codes.extend(['a', 'b', 'c', 'd', 'e', 'f'])
        color = [hex_codes[c // 16] + hex_codes[c % 16] for c in color]

        return '#' + ''.join(color)

    def get_fill_color(self, tree, node_id):
        if 'rgb' not in self.colors:
            self.colors['rgb'] = _color_brew(tree.n_classes[0])
            if tree.n_outputs != 1:
                self.colors['bounds'] = (np.min(-tree.impurity),
                                         np.max(-tree.impurity))
            elif (tree.n_classes[0] == 1 and
                  len(np.unique(tree.value)) != 1):
                self.colors['bounds'] = (np.min(tree.value),
                                         np.max(tree.value))
        if tree.n_outputs == 1:
            node_val = (tree.value[node_id][0, :] /
                        tree.weighted_n_node_samples[node_id])
            if tree.n_classes[0] == 1:
                node_val = tree.value[node_id][0, :]
        else:
            node_val = -tree.impurity[node_id]
        return self.get_color(node_val)

    def node_to_str(self, tree, node_id, criterion):
        if tree.n_outputs == 1:
            value = tree.value[node_id][0, :]
        else:
            value = tree.value[node_id]

        labels = (self.label == 'root' and node_id == 0) or self.label == 'all'

        characters = self.characters
        node_string = characters[-1]

        if self.node_ids:
            if labels:
                node_string += 'node '
            node_string += characters[0] + str(node_id) + characters[4]

        if tree.children_left[node_id] != _tree.TREE_LEAF:
            if self.feature_names is not None:
                feature = self.feature_names[tree.feature[node_id]]
            else:
                feature = "X%s%s%s" % (characters[1],
                                       tree.feature[node_id],
                                       characters[2])
            node_string += '%s %s %s%s' % (feature,
                                           characters[3],
                                           round(tree.threshold[node_id],
                                                 self.precision),
                                           characters[4])

        if self.impurity:
            if isinstance(criterion, _criterion.FriedmanMSE):
                criterion = "friedman_mse"
            elif not isinstance(criterion, six.string_types):
                criterion = "impurity"
            if labels:
                node_string += '%s = ' % criterion
            node_string += (str(round(tree.impurity[node_id], self.precision))
                            + characters[4])
        if labels:
            node_string += 'samples = '
        if self.proportion:
            percent = (100. * tree.n_node_samples[node_id] /
                       float(tree.n_node_samples[0]))
            node_string += (str(round(percent, 1)) + '%' +
                            characters[4])
        else:
            node_string += (str(tree.n_node_samples[node_id]) +
                            characters[4])

        if self.proportion and tree.n_classes[0] != 1:
            value = value / tree.weighted_n_node_samples[node_id]
        if labels:
            node_string += 'value = '
        if tree.n_classes[0] == 1:
            value_text = np.around(value, self.precision)
        elif self.proportion:
            value_text = np.around(value, self.precision)
        elif np.all(np.equal(np.mod(value, 1), 0)):
            value_text = value.astype(int)
        else:
            value_text = np.around(value, self.precision)
        
        value_text = str(value_text.astype('S32')).replace("b'", "'")
        value_text = value_text.replace("' '", ", ").replace("'", "")
        if tree.n_classes[0] == 1 and tree.n_outputs == 1:
            value_text = value_text.replace("[", "").replace("]", "")
        value_text = value_text.replace("\n ", characters[4])
        node_string += value_text + characters[4]

       
        if (self.class_names is not None and
                tree.n_classes[0] != 1 and
                tree.n_outputs == 1):
            if labels:
                node_string += 'class = '
            if self.class_names is not True:
                class_name = self.class_names[np.argmax(value)]
            else:
                class_name = "y%s%s%s" % (characters[1],
                                          np.argmax(value),
                                          characters[2])
            node_string += class_name

        if node_string.endswith(characters[4]):
            node_string = node_string[:-len(characters[4])]

        return node_string + characters[5]


class _MPLTreeExporter(_BaseTreeExporter):
    def __init__(self, max_depth=None, feature_names=None,
                 class_names=None, label='all', filled=False,
                 leaves_parallel=False, impurity=True, node_ids=False,
                 proportion=False, rotate=False, rounded=False,
                 special_characters=False, precision=3, fontsize=None):
        self.max_depth = max_depth
        self.feature_names = feature_names
        self.class_names = class_names
        self.label = label
        self.filled = filled
        self.leaves_parallel = leaves_parallel
        self.impurity = impurity
        self.node_ids = node_ids
        self.proportion = proportion
        self.rotate = rotate
        self.rounded = rounded
        self.special_characters = special_characters
        self.precision = precision
        self.fontsize = fontsize
        self._scaley = 10

        if isinstance(precision, Integral):
            if precision < 0:
                raise ValueError("'precision' debe ser mayor o igual a  0."
                                 " Pero {} tenemos.".format(precision))
        else:
            raise ValueError("'precision' debe ser un entero. Pero {}"
                             " tenemos.".format(type(precision)))

        self.ranks = {'leaves': []}
        self.colors = {'bounds': None}

        self.characters = ['#', '[', ']', '<=', '\n', '', '']

        self.bbox_args = dict(fc='w')
        if self.rounded:
            self.bbox_args['boxstyle'] = "round"
        self.arrow_args = dict(arrowstyle="<-")

    def _make_tree(self, node_id, et):
        name = self.node_to_str(et, node_id, criterion='entropy')
        if (et.children_left[node_id] != et.children_right[node_id]):
            children = [self._make_tree(et.children_left[node_id], et),
                        self._make_tree(et.children_right[node_id], et)]
        else:
            return Tree(name, node_id)
        return Tree(name, node_id, *children)

    def export(self, decision_tree, ax=None):
        import matplotlib.pyplot as plt
        from matplotlib.text import Annotation

        if ax is None:
            ax = plt.gca()
        ax.set_axis_off()
        my_tree = self._make_tree(0, decision_tree.tree_)
        dt = buchheim(my_tree)
        self._scalex = 1
        self.recurse(dt, decision_tree.tree_, ax)

        anns = [ann for ann in ax.get_children()
                if isinstance(ann, Annotation)]

        xys = [ann.xyann for ann in anns]

        mins = np.min(xys, axis=0)
        maxs = np.max(xys, axis=0)

        ax.set_xlim(mins[0], maxs[0])
        ax.set_ylim(maxs[1], mins[1])

        if self.fontsize is None:
            inv = ax.transData.inverted()
            renderer = ax.figure.canvas.get_renderer()
            for ann in anns:
                ann.update_bbox_position_size(renderer)
            widths = [inv.get_matrix()[0, 0]
                      * ann.get_bbox_patch().get_window_extent().width
                      for ann in anns]
            max_width = max(max(widths), 1)
            size = anns[0].get_fontsize() / max_width
            for ann in anns:
                ann.set_fontsize(size)

    def recurse(self, node, tree, ax, depth=0):
        kwargs = dict(bbox=self.bbox_args, ha='center', va='center',
                      zorder=100 - 10 * depth)

        if self.fontsize is not None:
            kwargs['fontsize'] = self.fontsize

        xy = (node.x * self._scalex, node.y * self._scaley)

        if self.max_depth is None or depth <= self.max_depth:
            if self.filled:
                kwargs['bbox']['fc'] = self.get_fill_color(tree,
                                                           node.tree.node_id)
            if node.parent is None:
                ax.annotate(node.tree.node, xy, **kwargs)
            else:
                xy_parent = (node.parent.x * self._scalex,
                             node.parent.y * self._scaley)
                kwargs["arrowprops"] = self.arrow_args
                ax.annotate(node.tree.node, xy_parent, xy, **kwargs)
            for child in node.children:
                self.recurse(child, tree, ax, depth=depth + 1)

        else:
            xy_parent = (node.parent.x * self._scalex, node.parent.y *
                         self._scaley)
            kwargs["arrowprops"] = self.arrow_args
            kwargs['bbox']['fc'] = 'grey'
            ax.annotate("\n  (...)  \n", xy_parent, xy, **kwargs)


class DrawTree(object):
    def __init__(self, tree, parent=None, depth=0, number=1):
        self.x = -1.
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(c, self, depth + 1, i + 1)
                         for i, c
                         in enumerate(tree.children)]
        self.parent = parent
        self.thread = None
        self.mod = 0
        self.ancestor = self
        self.change = self.shift = 0
        self._lmost_sibling = None
        self.number = number

    def left(self):
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]

    def lbrother(self):
        n = None
        if self.parent:
            for node in self.parent.children:
                if node == self:
                    return n
                else:
                    n = node
        return n

    def get_lmost_sibling(self):
        if not self._lmost_sibling and self.parent and self != \
                self.parent.children[0]:
            self._lmost_sibling = self.parent.children[0]
        return self._lmost_sibling
    lmost_sibling = property(get_lmost_sibling)

    def __str__(self):
        return "%s: x=%s mod=%s" % (self.tree, self.x, self.mod)

    def __repr__(self):
        return self.__str__()


def buchheim(tree):
    dt = firstwalk(DrawTree(tree))
    min = second_walk(dt)
    if min < 0:
        third_walk(dt, -min)
    return dt


def third_walk(tree, n):
    tree.x += n
    for c in tree.children:
        third_walk(c, n)


def firstwalk(v, distance=1.):
    if len(v.children) == 0:
        if v.lmost_sibling:
            v.x = v.lbrother().x + distance
        else:
            v.x = 0.
    else:
        default_ancestor = v.children[0]
        for w in v.children:
            firstwalk(w)
            default_ancestor = apportion(w, default_ancestor, distance)
        execute_shifts(v)

        midpoint = (v.children[0].x + v.children[-1].x) / 2

        w = v.lbrother()
        if w:
            v.x = w.x + distance
            v.mod = v.x - midpoint
        else:
            v.x = midpoint
    return v


def apportion(v, default_ancestor, distance):
    w = v.lbrother()
    if w is not None:
        vir = vor = v
        vil = w
        vol = v.lmost_sibling
        sir = sor = v.mod
        sil = vil.mod
        sol = vol.mod
        while vil.right() and vir.left():
            vil = vil.right()
            vir = vir.left()
            vol = vol.left()
            vor = vor.right()
            vor.ancestor = v
            shift = (vil.x + sil) - (vir.x + sir) + distance
            if shift > 0:
                move_subtree(ancestor(vil, v, default_ancestor), v, shift)
                sir = sir + shift
                sor = sor + shift
            sil += vil.mod
            sir += vir.mod
            sol += vol.mod
            sor += vor.mod
        if vil.right() and not vor.right():
            vor.thread = vil.right()
            vor.mod += sil - sor
        else:
            if vir.left() and not vol.left():
                vol.thread = vir.left()
                vol.mod += sir - sol
            default_ancestor = v
    return default_ancestor


def move_subtree(wl, wr, shift):
    subtrees = wr.number - wl.number
    wr.change -= shift / subtrees
    wr.shift += shift
    wl.change += shift / subtrees
    wr.x += shift
    wr.mod += shift


def execute_shifts(v):
    shift = change = 0
    for w in v.children[::-1]:
        w.x += shift
        w.mod += shift
        change += w.change
        shift += w.shift + change


def ancestor(vil, v, default_ancestor):
    if vil.ancestor in v.parent.children:
        return vil.ancestor
    else:
        return default_ancestor


def second_walk(v, m=0, depth=0, min=None):
    v.x += m
    v.y = depth

    if min is None or v.x < min:
        min = v.x

    for w in v.children:
        min = second_walk(w, m + v.mod, depth + 1, min)

    return min


class Tree(object):
    def __init__(self, node="", node_id=-1, *children):
        self.node = node
        self.width = len(node)
        self.node_id = node_id
        if children:
            self.children = children
        else:
            self.children = []
